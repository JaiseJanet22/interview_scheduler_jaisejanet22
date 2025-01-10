from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Availability
from .serializers import UserSerializer, AvailabilitySerializer
from datetime import datetime, timedelta

class RegisterAvailability(APIView):
    def post(self, request):
        serializer = AvailabilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GetAvailableSlots(APIView):
    def post(self, request):
        candidate_id = request.data.get('candidate_id')
        interviewer_id = request.data.get('interviewer_id')

        # Fetch availability slots for the candidate and interviewer
        candidate_slots = Availability.objects.filter(user_id=candidate_id)
        interviewer_slots = Availability.objects.filter(user_id=interviewer_id)

        common_slots = []

        for c_slot in candidate_slots:
            for i_slot in interviewer_slots:
                # Ensure the slots are on the same date
                if c_slot.date == i_slot.date:
                    # Convert time to datetime for arithmetic
                    c_start = datetime.combine(c_slot.date, c_slot.start_time)
                    c_end = datetime.combine(c_slot.date, c_slot.end_time)
                    i_start = datetime.combine(i_slot.date, i_slot.start_time)
                    i_end = datetime.combine(i_slot.date, i_slot.end_time)

                    # Determine the overlapping range
                    start = max(c_start, i_start)
                    end = min(c_end, i_end)

                    # Generate 1-hour slots within the overlapping range
                    while start + timedelta(hours=1) <= end:
                        slot_end = start + timedelta(hours=1)
                        common_slots.append([start.time().strftime('%H:%M:%S'), slot_end.time().strftime('%H:%M:%S')])
                        start = slot_end

        return Response({"common_slots": common_slots}, status=status.HTTP_200_OK)